import filter_users


def test():
    print("Filter users by age:")
    filter_users.filter_users_by_age(34)

    print("\nFilter users by email:")
    filter_users.filter_users_by_email("jordan.lee@example.com")

    print("\nFilter users by name:")
    filter_users.filter_users_by_name("Alex Morgan")


def main():
    test()

    query = (
        input("\nWhat would you like to filter by? (age, email, name): ")
        .strip()
        .lower()
    )

    print(f"\nFilter users by {query}:")

    if query == "name":
        filter_users.filter_users_by_name(input("Enter name: ").strip())
    elif query == "email":
        filter_users.filter_users_by_email(input("Enter email: ").strip())
    elif query == "age":
        filter_users.filter_users_by_age(int(input("Enter age: ")))


if __name__ == "__main__":
    main()
