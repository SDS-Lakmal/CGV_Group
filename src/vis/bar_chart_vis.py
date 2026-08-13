import matplotlib.pyplot as plt

def plot_student_history(dates, statuses):
    # Visualizing individual student attendance over time
    plt.figure(figsize=(7, 5))
    plt.bar(dates, [1 if s=='Present' else 0 for s in statuses], color='blue')
    plt.title('Student Attendance History')
    plt.ylabel('1 = Present, 0 = Absent')
    plt.savefig('output_member_8.png')
    print('Saved image as output_member_8.png')
    plt.show()