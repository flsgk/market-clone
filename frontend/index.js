const calcTime = (timestamp) => {
  const curTime = new Date().getTime() - 9 * 60 * 60 * 1000; // UTC에 맞추기 위해 - 9 시간 하기
  const time = new Date(curTime - timestamp);
  const hour = time.getHours();
  const minute = time.getMinutes();
  const second = time.getSeconds();

  if (hour > 0) return `${hour}시간 전`;
  else if (minute > 0) return `${minute}분 전`;
  else if (second > 0)
    return `${second}초 전`; // undefined 가 뜨지 않게 0도 대상에 포함
  else return "방금 전";
};

const renderData = (data) => {
  const main = document.querySelector("main");
  data
    .sort((a, b) => a - b)
    .forEach(async (obj) => {
      //.sort : 배열의 순서를 정렬하는 것
      //.reverse : 배열의 순서를 역으로 돌리는 것
      const Div = document.createElement("div");
      Div.className = "item-list";

      const imgDiv = document.createElement("div");
      imgDiv.className = "item-list__img";

      const img = document.createElement("img");
      const res = await fetch(`/images/${obj.id}`);
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      img.src = url;

      const InfoDiv = document.createElement("div");
      InfoDiv.className = "item-list__info";

      const InfoTitleDiv = document.createElement("div");
      InfoTitleDiv.className = "item-list__info-title";
      InfoTitleDiv.innerText = obj.title;

      const InfoMetaDiv = document.createElement("div");
      InfoMetaDiv.className = "item-list__info-meta";
      InfoMetaDiv.innerText = obj.place + " " + calcTime(obj.insertAt);

      const InfoPriceDiv = document.createElement("div");
      InfoPriceDiv.className = "item-list__info-price";
      InfoPriceDiv.innerText = obj.price;

      imgDiv.appendChild(img);

      InfoDiv.appendChild(InfoTitleDiv);
      InfoDiv.appendChild(InfoMetaDiv);
      InfoDiv.appendChild(InfoPriceDiv);

      Div.appendChild(imgDiv);
      Div.appendChild(InfoDiv);
      main.appendChild(Div);
    });
};

const fetchList = async () => {
  const res = await fetch("/items");
  const data = await res.json();
  renderData(data);
};

fetchList();
