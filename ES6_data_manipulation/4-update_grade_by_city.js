export default function updateStudentGradeByCity(students, city, grades) {
  return students
    .filter(student => student.location === city)
    .map(student => {
      const found = grades.find(grade => grade.studentId === student.id);
      return {
        ...student,
        grade: found ? found.grade : 'N/A'
      };
    });
}
