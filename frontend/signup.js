const form = document.querySelector("#signup-form");

const checkPassword = () => {
  const formData = new FormData(form);
  const password1 = formData.get("password");
  const password2 = formData.get("password2");
  if (password1 === password2) {
    return true;
  } else return false;
};

const handleSubmit = async (event) => {
  event.preventDefault(); //prevent redirect
  const formData = new FormData(form); // 무슨 뜻인지 모르겠음
  const sha256Password = sha256(formData.get("password")); //formdata 에서 password 값을 가져와서 sha256으로 변환한 다음
  formData.set("password", sha256Password); // password 값에 넣어준다.

  const div = document.querySelector("#info");

  if (checkPassword()) {
    // checkPassword()를 해서 비밀번호가 같으면
    const res = await fetch("/signup", {
      method: "post",
      body: formData, //넣어준 formdata를 body에 담아서 서버로 보낸다.
    });
    const data = await res.json(); // 서버로부터 data 를 받아왔을 때
    if (data === "200") {
      // 데이터가 200이면
      div.innerText = "회원가입에 성공했습니다.";
      div.style.color = "blue";
    }
  } else {
    // 그렇지 않으면
    div.innerText = "비밀번호가 일치하지 않습니다.";
    div.style.color = "red";
  }
};

form.addEventListener("submit", handleSubmit);
