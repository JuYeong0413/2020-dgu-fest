function limitSize(input) {
    if (input.files[0].size > (1*1024*1024)) {
        alert("파일 크기가 1mb를 넘습니다. 1mb이하의 파일만 등록이 가능합니다.");
        input.value = null;
    }

}