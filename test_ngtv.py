import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


falderin = '/home/user/tst'
falderout = '/home/user/out'


def test_ngt_unpack():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Error: Incorrect command'), 'Negative unpack test failed'


def test_ngt_check_arh():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Archive test failed'), 'Negative check archive test failed'

