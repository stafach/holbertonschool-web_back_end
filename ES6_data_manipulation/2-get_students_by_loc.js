export default function getStudentsByLocation(students, city) {
    const list = students.filter(student => student.location == city);
    return list;
}