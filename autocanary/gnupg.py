"""
AutoCanary | https://firstlook.org/code/autocanary
Copyright (c) 2015 First Look Media

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import subprocess, os, platform, tempfile, shutil, codecs

class GnuPG(object):

    def __init__(self):
        self.system = platform.system()
        self.creationflags = 0
        if self.system == 'Darwin':
            self.gpg_path = '/usr/local/bin/gpg'
        elif self.system == 'Linux':
            self.gpg_path = '/usr/bin/gpg2'
        elif self.system == 'Windows':
            import win32process
            self.creationflags = win32process.CREATE_NO_WINDOW
            self.gpg_path = '{0}\GNU\GnuPG\gpg2.exe'.format(os.environ['ProgramFiles(x86)'])

        self.gpg_command = [self.gpg_path, '--batch', '--no-tty']

    def is_gpg_available(self):
        if self.system == 'Windows':
            return os.path.isfile(self.gpg_path)
        else:
            return os.path.isfile(self.gpg_path) and os.access(self.gpg_path, os.X_OK)

    def seckeys_list(self):
        p = subprocess.Popen(self.gpg_command + ['--fingerprint', '--with-colons', '--list-secret-keys'], stdout=subprocess.PIPE, creationflags=self.creationflags)
        (stdoutdata, stderrdata) = p.communicate()
        gpg_output = stdoutdata.split(b'\n')

        seckeys = []
        for line in gpg_output:
            if line.startswith(b'fpr:'):
                fp = line.split(b':')[9]

                uids = []
                p = subprocess.Popen(self.gpg_command + ['--fingerprint', '--with-colons', '--list-keys', fp.decode()], stdout=subprocess.PIPE, creationflags=self.creationflags)
                if p.wait() != 0:
                  continue
                (stdoutdata, stderrdata) = p.communicate()
                gpg_output2 = stdoutdata.split(b'\n')

                for line in gpg_output2:
                    if line.startswith(b'pub:'):
                        validity = line.split(b':')[1]
                    if line.startswith(b'uid:'):
                        vals = line.split(b':')
                        uid_validity = vals[1]
                        uid = vals[9]
                        if uid_validity not in [b'i', b'd', b'r', b'e']:
                            uids.append(uid)

                if validity not in [b'i', b'd', b'r', b'e']:
                    seckeys.append({'fp': fp.decode(), 'uid':uids[0].decode()})

        return seckeys

    def sign(self, text, signing_fp):
        tempdir = tempfile.mkdtemp()

        # write message to file
        filename = '{0}/message'.format(tempdir)
        open(filename, 'w').write(text)

        # sign the file
        p = subprocess.Popen(self.gpg_command + ['--use-agent', '--default-key', signing_fp, '--no-emit-version', '--no-comments', '--clearsign', filename], creationflags=self.creationflags)
        returncode = p.wait()
        if returncode != 0:
            shutil.rmtree(tempdir)
            return False

        # read the signed message
        signed_filename = '{0}/message.asc'.format(tempdir)
        signed_message = codecs.open(signed_filename, 'r', 'utf-8').read()
        shutil.rmtree(tempdir)

        return signed_message
