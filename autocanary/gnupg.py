import subprocess, os, platform, tempfile, shutil

class GnuPG(object):

    def __init__(self):
        system = platform.system()
        if system == 'Darwin':
            self.gpg_path = '/usr/local/bin/gpg'
        elif system == 'Linux':
            self.gpg_path = '/usr/bin/gpg2'
        elif system == 'Windows':
            self.gpg_path = '{0}\GNU\GnuPG\gpg2.exe'.format(os.environ['ProgramFiles(x86)'])

        self.gpg_command = [self.gpg_path, '--batch', '--no-tty']

    def is_gpg_available(self):
        system = platform.system()
        if system == 'Windows':
            return os.path.isfile(self.gpg_path)
        else:
            return os.path.isfile(self.gpg_path) and os.access(self.gpg_path, os.X_OK)

    def seckeys_list(self):
        gpg_output = subprocess.check_output(self.gpg_command + ['--fingerprint', '--with-colons', '--list-secret-keys']).split('\n')

        seckeys = []
        for line in gpg_output:
            if line.startswith('fpr:'):
                fp = line.split(':')[9]

                uids = []
                gpg_output2 = subprocess.check_output(self.gpg_command + ['--fingerprint', '--with-colons', '--list-keys', fp]).split('\n')
                for line in gpg_output2:
                    if line.startswith('pub:'):
                        validity = line.split(':')[1]
                    if line.startswith('uid:'):
                        vals = line.split(':')
                        uid_validity = vals[1]
                        uid = vals[9]
                        if uid_validity not in ['i', 'd', 'r', 'e']:
                            uids.append(uid)

                if validity not in ['i', 'd', 'r', 'e']:
                    seckeys.append({'fp': fp, 'uid':uids[0]})

        return seckeys

    def sign(self, text, signing_fp):
        tempdir = tempfile.mkdtemp()

        # write message to file
        filename = '{0}/message'.format(tempdir)
        open(filename, 'w').write(text)

        # sign the file
        try:
            subprocess.check_call(self.gpg_command + ['--use-agent', '--default-key', signing_fp, '--clearsign', filename])
        except subprocess.CalledProcessError:
            shutil.rmtree(tempdir)
            return False

        # read the signed message
        signed_filename = '{0}/message.asc'.format(tempdir)
        signed_message = open(signed_filename, 'r').read()
        shutil.rmtree(tempdir)

        return signed_message
