function verifyEmail() {
  var email = document.getElementById('id_email').value;
  if (email.includes("@dgu.edu") || email.includes("@dgu.ac.kr") || email.includes("@dongguk.edu")) {
    return true;
  } else {
    alert("재학생 인증을 위해 동국대학교 웹메일을 입력해주세요.");
    return false;
  }
}