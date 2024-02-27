$(document).ready(function(){
    // 파일이 선택될 때마다 실행되는 함수
    $("#activityImage").change(function() {
        // 선택된 파일들의 이름을 가져와서 <div id="selectedPhotoName"></div>에 추가
        var selectedPhotoNames = "";
        for (var i = 0; i < this.files.length; i++) {
            selectedPhotoNames += '<p class="selectedPhotoName">' + this.files[i].name + "</p>";
        }
        $("#selectedPhotoName").html(selectedPhotoNames);
    });

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
        var profilePictureUrl = $(this).data("profile-photo-url");

        // 동적으로 profileSet 추가
        var newProfileSet = $('<div class="profileSet"></div>');
        newProfileSet.append('<img src="' + profilePictureUrl + '" alt="Profile Picture" class="profile-image">');
        newProfileSet.append('<input type="hidden" name="user_id" value="'+ profileName.trim() +'">');
        newProfileSet.append('<input type="text" name="user_say" id="user_say" class="sayinput">');

        // 선택한 프로필을 선택 목록에 추가
        $("#selectedUsers").append(newProfileSet);

        

        // addZone의 높이를 동적으로 늘리기
        var addZoneHeight = $("#addZone").height();
        $("#addZone").height(addZoneHeight + 30);
    });
});
