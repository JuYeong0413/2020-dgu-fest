function verifyStudentId() {
    var titleId = document.getElementById('title_id').value;
    if (titleId.length > 15) { 
      alert("공백포함 최대 15글자 입력가능합니다!");
      return false;
    }else return true;
  }