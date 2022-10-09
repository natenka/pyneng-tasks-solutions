import sqlite3
import sys

from tabulate import tabulate


def get_data_by_key_value(db_name, key, value):
    keys = "mac ip vlan interface switch".split()
    if key not in keys:
        print("This parameter is not supported.")
        print("Valid parameter values: {}".format(", ".join(keys)))
        return
    connection = sqlite3.connect(db_filename)

    query = "select * from dhcp where {} = ?".format(key)
    result = connection.execute(query, (value,))

    print("\nInformation about devices with the following parameters:", key, value)
    print(tabulate(result))


def get_all_data(db_name):
    print("The dhcp table has the following entries:")
    connection = sqlite3.connect(db_filename)
    print(tabulate(connection.execute("select * from dhcp")))


def parse_args(db_name, args):
    if len(args) == 0:
        get_all_data(db_filename)
    elif len(args) == 2:
        key, value = args
        get_data_by_key_value(db_filename, key, value)
    else:
        print("Please enter two or zero arguments")


if __name__ == "__main__":
    db_filename = "dhcp_snooping.db"
    args = sys.argv[1:]
    parse_args(db_filename, args)
