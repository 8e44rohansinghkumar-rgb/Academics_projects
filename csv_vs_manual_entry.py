import pandas as pd

def manual_entry():
    data = []
    n = int(input("How many students? "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = int(input(f"Enter marks for {name}: "))
        data.append([name, marks])
    return pd.DataFrame(data, columns=["Name", "Marks"])

def load_csv():
    path = input("Enter CSV file path: ")
    try:
        df = pd.read_csv(path)
        if "Name" not in df.columns or "Marks" not in df.columns:
            df.columns = ["Name", "Marks"]  # assume first 2 columns
        return df
    except Exception as e:
        print("Error loading CSV:", e)
        return None

def assign_grade(m):
    if m >= 90: return "A"
    elif m >= 80: return "B"
    elif m >= 70: return "C"
    elif m >= 60: return "D"
    else: return "F"

def analyze(df):
    print("\n--- ANALYSIS SUMMARY ---")
    print(f"Total Students : {len(df)}")
    print(f"Average Marks  : {df['Marks'].mean():.2f}")
    print(f"Median Marks   : {df['Marks'].median():.2f}")
    print(f"Highest Marks  : {df['Marks'].max()}")
    print(f"Lowest Marks   : {df['Marks'].min()}")

    df["Grade"] = df["Marks"].apply(assign_grade)
    print("\nGrade Distribution:")
    print(df["Grade"].value_counts().sort_index())

    passed = df[df["Marks"] >= 40]
    failed = df[df["Marks"] < 40]
    print(f"\nPassed: {len(passed)} students")
    print(f"Failed: {len(failed)} students")

    print("\n--- RESULTS TABLE ---")
    print(df.sort_values(by="Marks", ascending=False).to_string(index=False))

    return df

def main():
    print("Welcome to GradeBook Analyzer (Simple Version)")
    while True:
        print("\n1. Manual Entry\n2. Load from CSV\n3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            df = manual_entry()
        elif choice == "2":
            df = load_csv()
            if df is None:
                continue
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        df = analyze(df)

        exp = input("\nExport results to CSV? (y/n): ").lower()
        if exp == "y":
            out = input("Enter output filename (e.g. results.csv): ")
            df.to_csv(out, index=False)
            print("Results exported successfully!")

        again = input("\nAnalyze another dataset? (y/n): ").lower()
        if again != "y":
            print("Exiting program. Bye!")
            break

if __name__ == "__main__":
    main()