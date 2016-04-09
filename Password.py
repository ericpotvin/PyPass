""" Encrypt and Decrypt Passwords

    Example

    my_pass = Password("pass", "base64")
    print my_pass.encrypt_text("hi")
    print my_pass.decrypt_text("aGk=")

"""
import subprocess


class Password(object):
    """ Password Class
    """

    SHELL_EXT = ".sh"
    ENCRYPTED_FILE_SUFFIX = ".enc"

    def __init__(self, pass_key, mode, digest):
        self.pass_key = pass_key
        self.mode = mode
        self.digest = digest

    def encrypt_text(self, raw_text):
        """ Encrypt a string
            encrypt_text.sh "string_to_encrypt" "password" "mode"
            :param raw_text: the text
        """
        return self._run_command("encrypt_text", raw_text)

    def decrypt_text(self, encrypted_text):
        """ Decrypt a string
            decrypt_text.sh "string_to_encrypt" "password" "mode"
            :param encrypted_text: the encrypted text
        """
        return self._run_command("decrypt_text", encrypted_text)

    def _run_command(self, cmd, text):
        """ run the command
            :param cmd: The program to run
            :param text: The text to encrypt
        """
        cmd = "./%s%s" % (cmd, self.SHELL_EXT)

        process = subprocess.Popen(
            [cmd, text, self.pass_key, self.mode, self.digest],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = process.communicate()

        if err:
            return "ERROR: %s" % err
        return out.strip()

    @staticmethod
    def get_cipher_list():
        """ Get the cipher list
            CTR is used if you want good parallelization (speed)
            OFB/CFB is better because you only need encryption, not decryption
            :return: list
        """
        return [
            "aes-128-cbc",
            "aes-192-cbc",
            "aes-256-cbc",
            "base64",
            "bf",
            "bf-cbc",
            "bf-cfb",
            "bf-ofb",
            "camellia-128-cbc",
            "camellia-192-cbc",
            "camellia-256-cbc",
            "cast",
            "cast-cbc",
            "cast5-cbc",
            "cast5-cfb",
            "cast5-ofb",
            "des",
            "des-cbc",
            "des-cfb",
            "des-ede",
            "des-ede-cbc",
            "des-ede-cfb",
            "des-ede-ofb",
            "des-ede3",
            "des-ede3-cbc",
            "des-ede3-cfb",
            "des-ede3-ofb",
            "des-ofb",
            "des3",
            "desx",
            "rc2",
            "rc2-40-cbc",
            "rc2-64-cbc",
            "rc2-cbc",
            "rc2-cfb",
            "rc2-ofb",
            "rc4",
            "rc4-40",
            "seed",
            "seed-cbc",
            "seed-cfb",
            "seed-ofb"]

    @staticmethod
    def get_digest_list():
        """ Get the digest list
            :return: list
        """
        return [
            "md4",
            "md5",
            "ripemd160",
            "sha",
            "sha1",
            "sha224",
            "sha256",
            "sha384",
            "sha512",
            "whirlpool"]
