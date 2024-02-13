document.addEventListener("DOMContentLoaded", function() {
    var profiles = [
        { name: "John Doe", profileImage: "john.jpg", githubLink: "https://github.com/johndoe", profilePage: "profile1.html" },
        { name: "Jane Smith", profileImage: "jane.jpg", githubLink: "https://github.com/janesmith", profilePage: "profile2.html" },
        // 다른 프로필 데이터들...
    ];

    var profileContent = document.getElementById("profileContent");

    profiles.forEach(function(profile) {
        var imageElement = document.createElement("img");
        imageElement.src = profile.profileImage;
        imageElement.alt = "Profile Picture";

        // 이미지를 클릭했을 때 프로필 페이지로 이동하는 이벤트를 추가합니다.
        imageElement.addEventListener("click", function() {
            window.location.href = "profile.html"; // 프로필 페이지로 이동
        });

        // 프로필 이미지를 프로필 컨텐츠 영역에 추가합니다.
        profileContent.appendChild(imageElement);
    });

});
