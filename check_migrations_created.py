import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manage-path', type=str, default='./src/manage.py')
    parser.add_argument('--exec-command', type=str, default='python3')
    args = parser.parse_args()

    pre_command = ''
    if any([part in ['poetry', 'pipenv'] for part in args.exec_command.split(' ')]):
        # unsetting hooks virtualenv path from env variables so it does 
        # NOT get used when calling poetry or pipenv
        pre_command = 'unset VIRTUAL_ENV; '

    output = subprocess.check_output(
        f'{pre_command}{args.exec_command} {args.manage_path} makemigrations --dry-run',
        shell=True
    ).decode('utf-8')
    if output.strip() == 'No changes detected':
        return 0
    print('\033[91mMigrations were not created!\033[0m')
    return 1


if __name__ == '__main__':
    exit(main())
