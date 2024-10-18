const form = document.querySelector("#login-form");

const handleSubmit = async (event) => {
  event.preventDefault(); //prevent redirect
  const formData = new FormData(form); // 무슨 뜻인지 모르겠음
  const sha256Password = sha256(formData.get("password")); //formdata 에서 password 값을 가져와서 sha256으로 변환한 다음
  formData.set("password", sha256Password); // password 값에 넣어준다.

  const res = await fetch("/login", {
    method: "post",
    body: formData, //넣어준 formdata를 body에 담아서 서버로 보낸다.
  });
  const data = await res.json(); // 서버로부터 data 를 받아왔을 때
  // if (data === "200") {
  //   // 데이터가 200이면
  //   alert("로그인에 성공했습니다.");
  //   window.location.pathname = "/login.html";
  // }
};

form.addEventListener("submit", handleSubmit);
