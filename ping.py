from subprocess import check_output, CalledProcessError

FILENAME = 'ips.txt'
PING_COMMAND = 'ping -q -c 3 -W 1'


def ping(ip):
    cmd = f'{PING_COMMAND} {ip}'
    split_cmd = cmd.split()

    print(f'running: {cmd}')

    try:
        check_output(split_cmd)

    except CalledProcessError:
        print(f'{ip} is UNREACHABLE!')

        return

    print(f'{ip} is reachable')


def main():
    with open(FILENAME, 'r') as f:
        ips = f.read().splitlines()

    for ip in ips:
        ping(ip)


if __name__ == '__main__':
    main()