from phone_book import PhoneBook


class TestPhoneBook:
    def test_all(self):
        phone_book = PhoneBook(
            records=[
                ("John Doe", "03 234 567 890"),
                ("Mary Doe", "01 234 567 890"),
                ("Donald Doe", "02 234 567 890"),
            ]
        )

        previous = ""

        for record in phone_book.all():
            assert record[0] > previous
            previous = record[0]

    def test_add(self):
        record = ("John Doe", "01 234 567 890")
        phone_book = PhoneBook(
            records=[
                ("Marry Doe", "01 234 567 890"),
                ("Donald Doe", "02 234 567 890"),
            ]
        )
        phone_book.add(record)

        assert record in phone_book.all()
