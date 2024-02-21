document.addEventListener("DOMContentLoaded", function() {
    var profiles = [
        { name: "John Doe", profileImage: "{% static 'img/pic1.jpg' %}", githubLink: "https://github.com/johndoe", profilePage: "profile1.html" },
        { name: "Jane Smith", profileImage: "{% static 'img/pic1.jpg' %}", githubLink: "https://github.com/janesmith", profilePage: "profile2.html" },
        // 다른 프로필 데이터들...
    ];

    // 이미지 요소들에 클릭 이벤트를 추가합니다.
    var images = document.querySelectorAll(".person img");
    images.forEach(function(image, index) {
        // 각 이미지를 클릭했을 때 프로필 페이지로 이동하는 이벤트를 추가합니다.
        image.addEventListener("click", function() {
            // 해당 프로필의 프로필 페이지 URL로 이동합니다.
            window.location.href = '/profile/' + profiles[index].username + '/';

        });
    });

});
