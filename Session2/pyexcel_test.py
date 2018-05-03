import pyexcel

data = [
    {
        "Name": "Huyen",
        "Age" : 23
    },
    {
        "Name": "Duc",
        "Age" : 19
    },
    {
        "Name": "Truong",
        "Age" : 22
    },

]

pyexcel.save_as(records = data, dest_file_name = "test.xlsx")
