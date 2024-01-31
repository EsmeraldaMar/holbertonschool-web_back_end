export default function updateStudentGradeByCity(
  listStudents,
  city,
  newGrades,
) {
  if (!Array.isArray(listStudents)) {
    return [];
  }
  return listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter(
        (grade) => grade.studentId === student.id,
      )[0];
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
