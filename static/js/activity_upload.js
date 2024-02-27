// activity_upload.js

$(document).ready(function(){
    // "사람 추가" 버튼 클릭 시 모달 열기
    $("#choicePeople").click(function(){
        $("#myModal").css("display", "block");
    });

    // 모달 닫기 버튼 클릭 시 모달 닫기
    $("#closeModal").click(function(){
        $("#myModal").css("display", "none");
    });

    // 프로필 선택 시 처리
    $(".profile-item").click(function() {
        var profileId = $(this).data("profile-id");
        var profileName = $(this).text();
        var profilePictureUrl = $(this).data("profile-photo-url"); // 프로필 사진 URL 가져오기

        // 동적으로 profileSet 추가
        var newProfileSet = $('<div class="profileSet"></div>');
        newProfileSet.append('<div><img src="' + profilePictureUrl + '" alt="Profile Picture" class="profile-image"></div>');
        newProfileSet.append('<div><p>' + profileName + '</p></div>');
        newProfileSet.append('<input type="hidden" name="user_id" value="">' + profileName + '</p></div>');

        // 선택한 프로필을 선택 목록에 추가
        $("#selectedUsers").append(newProfileSet);

        // 선택한 프로필 정보를 선택 목록에 추가
        $("#selectedProfiles").append('<input type="hidden" name="selected_profiles[]" value="' + profileId + '">');
        var newUserInput = $('<div class="userinput"></div>');
        newUserInput.append('<label for="user_say_' + profileId + '">사용자의 말:</label>');
        newUserInput.append('<input type="text" name="user_say_' + profileId + '" id="user_say_' + profileId + '">');

        $("#profileSet").append(newUserInput);
    });
});
