import pandas as pd

array_data = [10, 20, 30, 40]
series_from_array = pd.Series(array_data)
print("Series from Array:\n", series_from_array)

dict_data = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:\n", series_from_dict)

student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22],
    'Marks': [85, 90, 95]
}
student_df = pd.DataFrame(student_data)
print("\nStudent DataFrame:\n", student_df)

empty_df = pd.DataFrame()
print("\nEmpty DataFrame:\n", empty_df)

empty_with_cols = pd.DataFrame(columns=['Name', 'Age', 'Marks'])
print("\nEmpty DataFrame with Columns:\n", empty_with_cols)

student_df.to_excel("student_data.xlsx", index=False)
print("\nDataFrame has been written to 'student_data.xlsx'")
