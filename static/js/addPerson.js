var profileElement = document.createElement("div");
profileElement.classList.add("person");

var imageElement = document.createElement("img");
imageElement.src = "{% if profile.profile_photo %}{{ profile.profile_photo.url }}{% else %}{% static 'img/default_profile.jpg' %}{% endif %}";
imageElement.alt = "Profile Picture";

var nameElement = document.createElement("h2");
nameElement.textContent = "{{ request.user.first_name }}{{ request.user.last_name }}";

var linkElement = document.createElement("a");
linkElement.href = "{{ profile.github }}";
linkElement.textContent = "깃허브링크";

// 프로필 요소에 이미지, 이름, 링크를 추가합니다.
profileElement.appendChild(imageElement);
profileElement.appendChild(nameElement);
profileElement.appendChild(linkElement);

// 프로필 리스트 컨테이너에 프로필 요소를 추가합니다.
personListContainer.appendChild(profileElement);