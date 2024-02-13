document.addEventListener("DOMContentLoaded", function() {
    // 프로필 데이터. (임시로 배열 사용. 추후에 어드민에서 데이터 받아오는 걸로 바꿔야 함)
    var profiles = [
        { name: "John Doe", profileImage: "john.jpg", githubLink: "https://github.com/johndoe" },
        { name: "Jane Smith", profileImage: "jane.jpg", githubLink: "https://github.com/janesmith" },
        { name: "Jane Smith", profileImage: "jane.jpg", githubLink: "https://github.com/janesmith" },
    ];

    var personListContainer = document.getElementById("personList");

    // 각 프로필 데이터를 반복하며 프로필 요소를 생성합니다.
    profiles.forEach(function(profile) {
        var profileElement = document.createElement("div");
        profileElement.classList.add("person");
        
        var imageElement = document.createElement("img");
        imageElement.src = profile.profileImage;
        imageElement.alt = "Profile Picture";

        var nameElement = document.createElement("h2");
        nameElement.textContent = profile.name;

        var linkElement = document.createElement("a");
        linkElement.href = profile.githubLink;
        linkElement.textContent = "Github Link";

        // 프로필 요소에 이미지, 이름, 링크를 추가합니다.
        profileElement.appendChild(imageElement);
        profileElement.appendChild(nameElement);
        profileElement.appendChild(linkElement);

        // 프로필 리스트 컨테이너에 프로필 요소를 추가합니다.
        personListContainer.appendChild(profileElement);
    });
});
