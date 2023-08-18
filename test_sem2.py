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


def test_step1():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Everything is Ok'), 'test1 Fail'


def test_step2():
    assert checkout(f'cd {falderin}; 7z u {falderout}/arh1', 'Everything is Ok'), 'test2 Fail'


def test_step3():
    assert checkout(f'cd {falderin}; 7z d {falderout}/arh1', 'Everything is Ok'), 'test3 Fail'


def test_step4():
    assert checkout(f'cd {falderin}; 7z l {falderout}/arh1', 'File1.txt'), 'test4 Fail'


def test_step5():
    assert checkout(f'cd {falderin}; 7z x {falderout}/arh1', 'Everything is Ok'), 'test5 Fail'

