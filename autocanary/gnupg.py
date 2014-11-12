import subprocess, os, platform, tempfile, shutil

class GnuPG(object):

    def __init__(self):
        system = platform.system()
        if system == 'Darwin':
            self.gpg_path = '/usr/local/bin/gpg'
        elif system == 'Linux':
            self.gpg_path = '/usr/bin/gpg'

        self.gpg_command = [self.gpg_path, '--batch', '--no-tty']

        # for suppressing output
        self.devnull = open('/dev/null', 'w')

    def is_gpg_available(self):
        return os.path.isfile(self.gpg_path) and os.access(self.gpg_path, os.X_OK)

    def seckeys_list(self):
        gpg_output = subprocess.check_output(self.gpg_command + ['--fingerprint', '--with-colons', '--list-secret-keys']).split('\n')

        seckeys = []
        for line in gpg_output:
            if line.startswith('sec:'):
                vals = line.split(':')
                keyid = vals[4]
                uid = vals[9]
                seckeys.append({'keyid': keyid, 'uid':uid})

        return seckeys

    def sign(self, text, signing_keyid):
        tempdir = tempfile.mkdtemp()

        # write message to file
        filename = '{0}/message'.format(tempdir)
        open(filename, 'w').write(text)

        # sign the file
        try:
            subprocess.check_call(self.gpg_command + ['--use-agent', '--default-key', signing_keyid, '--clearsign', filename])
        except subprocess.CalledProcessError:
            shutil.rmtree(tempdir)
            return False

        # read the signed message
        signed_filename = '{0}/message.asc'.format(tempdir)
        signed_message = open(signed_filename, 'r').read()
        shutil.rmtree(tempdir)

        return signed_message

