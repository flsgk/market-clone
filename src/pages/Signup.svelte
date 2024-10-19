<form id="signup-form" action="/signup" method="post">
  <!-- 폼을 어느 주소로 보낼 건지를 입력하는 부분 : 주소에 /signup.html을 압력하면 확인 가능 -->
  <div>
    <h1>회원가입</h1>
  </div>

  <div>
    <label for="id">아이디</label>
    <input type="text" id="id" name="id" required />
  </div>
  <div>
    <label for="password">비밀번호</label>
    <input type="password" id="password" name="password" required />
  </div>
  <div>
    <label for="password2">비밀번호 확인</label>
    <input type="password" id="password2" name="password2" required />
  </div>
  <div>
    <label for="name">이름</label>
    <input type="text" id="name" name="name" required />
  </div>
  <div>
    <label for="email">이메일</label>
    <input type="email" id="email" name="email" required />
  </div>
  <div>
    <button type="submit">회원가입 하기</button>
  </div>
  <div id="info"></div>
</form>
