import matplotlib.pyplot as plt

def plot_attendance_pie(present_count, absent_count):
    labels = ['Present', 'Absent']
    sizes = [present_count, absent_count]
    colors = ['#4CAF50', '#F44336']
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Daily Attendance Summary')
    plt.savefig('output_member_7.png')
    print('Saved image as output_member_7.png')
    plt.show()