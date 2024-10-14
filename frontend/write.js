const form = document.getElementById("write-form");
// id를 통해서 form 요소를 가져오는 것

const handleSubmitForm = async (event) => {
  event.preventDefault();

  const body = new FormData(form);
  body.append("insertAt", new Date().getTime());

  try {
    const res = await fetch("/items", {
      method: "POST",
      body,
      // 맨 윗 줄에서 선택한 form 값을 넣어서 보내준다
    });
    const data = await res.json();
    if (data === "200") window.location.pathname = "/"; //데이터를 json 형식으로 바꾸고, 200이라면 경로를 '/'로 바꾼다.
  } catch (e) {
    console.error(e); // 그렇지 않으면 에러를 출력한다.
  }
};

form.addEventListener("submit", handleSubmitForm);
//submit 이라는 이벤트를 하면, handleSubmitForm이라는 함수를 실행한다.
