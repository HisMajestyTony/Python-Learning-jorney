grades = {
    "Anna": [5,6,6],
    "John": [4,5,6],
    "Mike": [3,4,5]
}

anna = sum(grades.get("Anna")) / len(grades.get("Anna"))
john = sum(grades.get("John")) / len(grades.get("John"))
mike = sum(grades.get("Mike")) / len(grades.get("Mike"))

print(f'Anna: {anna:,.2f}')
print(f'John: {john:,.2f}')
print(f'Mike: {mike:,.2f}')