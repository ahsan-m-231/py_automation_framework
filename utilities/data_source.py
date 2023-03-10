from utilities import read_data

# test_data = [("admin", "pass", "English (Standard)", "OpenEMR")]
test_data = [("admin", "pass", "English (Standard)", "OpenEMR"),
             ("physician", "physician", "English (Standard)", "OpenEMR"),
             ("accountant", "pass", "English (Standard)", "OpenEMR")]

print("list length....", len(test_data))
print("list length 1....", test_data[0])
print("list length 2....", test_data[1])
# print("list length 3....", test_data[2])


test_invalid_data = [("admin", "pass", "Dutch", "OpenEMR"),
                     ("physician", "physician", "Greek", "OpenEMR"),
                     ("accountant", "pass", "Arabic", "OpenEMR")]


from utilities import read_data

test_valid_login_data = [
    ("admin", "pass", "English (Indian)", "OpenEMR"),
    ("physician", "physician", "English (Indian)", "OpenEMR"),
    ("accountant", "accountant", "English (Indian)", "OpenEMR")
]

test_invalid_login = [["john", "john123", "Dutch", "Invalid username or password"],
                      ["peter", "peter123", "Greek", "Invalid username or password"]]

test_valid_login_data_csv = read_data.get_csv_data("../test_data/test_valid_login.csv")

test_valid_login_data_excel = read_data.get_excel_data("../test_data/open_emr_data.xlsx", "test_valid_login")