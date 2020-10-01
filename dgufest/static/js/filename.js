var mediafile =  document.getElementById("onlyFileName").innerHTML;
(function deleteParentdir(){
    var mediaArray = mediafile.split('/');
    document.getElementById("onlyFileName").innerHTML = mediaArray[1];
})()

  
