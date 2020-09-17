function limitSize(input) {
    if (input.files[0].size > (1*1024*1024)) {
        alert("파일 사이즈가 1mb를 넘습니다.");
        input.value = null;
    }

}