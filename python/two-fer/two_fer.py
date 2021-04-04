def twofer(*name):
    if len(name):
        return f'One for {name[0]}, one for me.'
    else:
        return 'One for you, one for me.'

def main():
    twofer('Alice')
    twofer()

if __name__ == "__main__":
    main()
