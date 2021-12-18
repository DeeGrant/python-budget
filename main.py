from statement import Statement


def main():
    st = Statement()
    st.load()
    st.balance()
    print(st.transactions.to_string())


if __name__ == "__main__":
    main()
