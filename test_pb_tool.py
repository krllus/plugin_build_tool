import os

import click
from click.testing import CliRunner
from pb_tool import pb_tool

runner = CliRunner()


def test_validate():
    result = runner.invoke(pb_tool.cli, ['validate'])
    assert result.exit_code == 0


def test_clean():
    result = runner.invoke(pb_tool.cli, ['clean'])
    assert result.exit_code == 0


def test_clean_docs():
    result = runner.invoke(pb_tool.cli, ['clean_docs'])
    assert result.exit_code == 0


def test_config():
    result = runner.invoke(pb_tool.cli,
                           ['config', '--name', 'test_from_pytest.cfg',
                            '--package', 'testname'], input='y\n')
    assert result.exit_code == 0
    assert os.path.exists('test_from_pytest.cfg') == 1


def test_doc():
    result = runner.invoke(pb_tool.cli, ['doc'])
    assert result.exit_code == 0


def test_deploy():
    result = runner.invoke(pb_tool.cli, ['deploy'], input='y\n')
    assert result.exit_code == 0


def test_zip():
    result = runner.invoke(pb_tool.cli, ['zip'], input='y\n')
    assert result.exit_code == 0
    # assert os.path.exists(os.path.join(os.getcwd(), 'whereami.zip'))


def test_dclean():
    result = runner.invoke(pb_tool.cli, ['dclean'], input='y\n')
    assert result.exit_code == 0


def test_help():
    result = runner.invoke(pb_tool.cli, ['help'])
    assert result.exit_code == 0


def test_list():
    result = runner.invoke(pb_tool.cli, ['list'])
    assert result.exit_code == 0


def test_update():
    result = runner.invoke(pb_tool.cli, ['update'])
    assert result.exit_code == 0


def test_version():
    result = runner.invoke(pb_tool.cli, ['version'])
    assert result.exit_code == 0


def test_compile():
    result = runner.invoke(pb_tool.cli, ['compile'])
    assert result.exit_code == 0


if __name__ == '__main__':
    test_update()

    test_validate()
    test_clean()
    test_clean_docs()
    test_config()
    test_doc()
    test_deploy()
    test_zip()
    test_dclean()
    test_help()
    test_list()

    test_version()
    test_compile()
