function fileCheck(input) {
    if (input.files[0].size > (300*1024*1024)) {
        alert("파일 크기가 300mb를 넘습니다. 300mb이하의 파일만 등록이 가능합니다.");
        input.value = null;
        
    } else if (input.files && input.files[0]) {
        let reader = new FileReader();
        let fileType = input.files[0].type;
        let imageElement = document.getElementById('show-image-tag')
        let videoElement = document.getElementById('show-video-tag')
        reader.onload = function (e) {
            e.preventDefault()
            if (fileType.includes('image') === true) {
                if (imageElement !== null) {imageElement.remove();}
                if (videoElement !== null) {videoElement.remove();}

                let newImage = document.createElement("img"); 
                $(newImage).attr('id', 'show-image-tag');
                $(newImage).attr('src', e.target.result);
                $(newImage).css('width', '50%');
                
                $("#content").append(newImage);
            } else if( fileType.includes('video') === true) {
                if (imageElement !== null) {imageElement.remove();}
                if (videoElement !== null) {videoElement.remove();}

                let newVideo = document.createElement("video"); 
                $(newVideo).attr('id', 'show-video-tag');
                $(newVideo).attr('controls', ' ');
                $(newVideo).attr('preload', 'auto');
                $(newVideo).css('width', '50%');
                
                source = document.createElement('source');
                $(source).attr('type', fileType);
                $(source).attr('src', e.target.result);
                
                $("#content").append(newVideo);
                $(newVideo).append(source);
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}


function showFile() {
    $(document).ready(function () {

    })
}