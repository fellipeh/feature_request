from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b"gAAAAABcngzoyogoMRb7P8aggE49_8EwsJy_wDrCIGR2PuE2wFhDJ9KDOkNf1OG_xEUvvTT8BCfgo_ROLPCfJuK5" \
          b"-JmU318Kw5KYbfkn6MBFdE4LsS0iGVa9EFtVroqQcJqW8H95yfyQM" \
          b"-pEwT6kVtKdrxciyXHg0UVdLbMiKmc7VwrrLHmcINIuYaXGMuXuLz6zrx5nQL77 "


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
