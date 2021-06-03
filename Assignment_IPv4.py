def validation_IP(file):
    try:
        f = open(file, 'r')
        for line in f:
            if '.' not in line or line.count('.') != 3 or len(line) > 15 or any(
                    [True if int(i) < 0 or int(i) > 255 else False for i in line.split(".")]):
                invalid = line.strip("\n")
                print(f"{invalid} Not a valid IPv4 Address")
            else:
                if line.split(".")[0] == str(224):
                    multi_cast = line.strip("\n")
                    print(f"{multi_cast} Multicast address")
                elif line.split(".")[0] == str(224) and line.split(".")[-1] == str(2):
                    all_routers = line.strip("\n")
                    print(f"{all_routers} All routers on this IP")
                else:
                    valid = line.strip("\n")
                    print(f"{valid} Valid IPv4 Address")

        f.close()
    except IOError as e:
        print(e)

def main():
    validation_IP('data.txt')


if __name__ == "__main__":
    main()