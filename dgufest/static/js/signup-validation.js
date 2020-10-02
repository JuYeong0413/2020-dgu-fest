function verifyValues() {
  if (verifyStudentId() && verifyPhone()) return true;
  else return false;
}

function verifyStudentId() {
  var studentId = document.getElementById('id_student_id').value;
  if (studentId.length != 10) { // 10자리 확인
    alert("10자리의 학번을 입력해주세요.");
    return false;
  } else if (!studentId.startsWith("20")) { // 20xx으로 시작하는지 확인
    alert("학번을 확인해주세요.");
    return false;
  }else return true;
}

function verifyPhone() {
  var phoneNumber = document.getElementById('id_phone_number').value;
  if (phoneNumber.length != 11) {
    alert("핸드폰번호를 확인해주세요.");
    return false;
  } else if (!phoneNumber.unique) {
    alert("이미 가입 된 번호입니다.");
  } else return true;
}