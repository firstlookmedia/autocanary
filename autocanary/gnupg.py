import subprocess, os, tempfile, shutil

class GnuPG(object):

    def __init__(self):
        self.gpg_path = '/usr/local/bin/gpg'
        self.gpg_command = [self.gpg_path, '--batch', '--no-tty']

        # for suppressing output
        self.devnull = open('/dev/null', 'w')

    def is_gpg_available(self):
        return os.path.isfile(self.gpg_path) and os.access(self.gpg_path, os.X_OK)

    def seckeys_list(self):
        gpg_output = subprocess.check_output(self.gpg_command + ['--fingerprint', '--with-colons', '--list-secret-keys']).split('\n')

        seckeys = []
        for line in gpg_output:
            if line.startswith('fpr:'):
                fp = line.split(':')[9]
                seckeys.append({'fp': fp, 'uids':[]})

        for i,seckey in enumerate(seckeys):
            fp = seckey['fp']
            gpg_output = subprocess.check_output(self.gpg_command + ['--with-colons', '--list-secret-keys', fp]).split('\n')

            for line in gpg_output:
                if line.startswith('uid:'):
                    uid = line.split(':')[9]
                    seckeys[i]['uids'].append(uid)

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

