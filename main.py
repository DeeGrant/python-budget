from statement import Statement


def main():
    st = Statement(balance=50000)
    st.load()
    st.balance()
    print(st.ledger.to_string())

    st.plot()
    st.spending()


if __name__ == "__main__":
    main()
