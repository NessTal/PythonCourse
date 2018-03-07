def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """

    result = {}
    for s in subj1_all_students.keys():
        if subj2_all_students.get(s) != None:
            g_max_1 = max(subj1_all_students.get(s))
            g_max_2 = max(subj2_all_students.get(s))
            if g_max_1 > g_max_2:
                result[s] = 'subj1'
            elif g_max_1 < g_max_2:
                result[s] = 'subj2'
            else:
                result[s] = 'equal'

    return result


if __name__ == '__main__':
    # Question 2
    subj1_all_students = {'A':[100,90],'B':[70,80],'C':[60,50],'D':[30,40]}
    subj2_all_students = {'A':[99,89], 'B':[71,81],'C':[60,55],'E':[31,41]}
    return_value = compare_subjects_within_student(subj1_all_students,subj2_all_students)

    print(f"Question 2 solution: {return_value}")
