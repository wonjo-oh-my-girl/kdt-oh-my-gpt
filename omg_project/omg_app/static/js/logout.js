// 로그인되어있을 때 로그인 버튼 비활성화 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


// 로그아웃 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

const proFileLogout = document.getElementById('logout-buttons')

proFileLogout.addEventListener('click', logout)


async function logout() {
    const logout_response = await fetch('http://oh-my-gpt.com/api/logout')

    if (logout_response.status == 200) {
        alert('로그아웃 되었습니다.')
        location.href = 'http://oh-my-gpt.com/'
    }
}