<script>
  import { onMount } from "svelte";
  import Footer from "../components/footer.svelte";
  import { getDatabase, ref, onValue } from "firebase/database";

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

  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  $: items = [];

  const db = getDatabase();
  const itemsRef = ref(db, "items/");
  onMount(() => {
    onValue(itemsRef, (snapshot) => {
      const data = snapshot.val();
      items = Object.values(data).reverse();
    });
  });
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/chart-bar.svg" alt="chart-bar" />
      <img src="assets/wifi.svg" alt="wifi" />
      <img src="assets/battery.svg" alt="battery" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div>역삼 1동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow.svg" alt="arrow" />
      </div>
    </div>
    <div class="menu-bar__icons">
      <img src="assets/search.svg" alt="search" />
      <img src="assets/menu.svg" alt="menu" />
      <img src="assets/alert.svg" alt="alert" />
    </div>
  </div>
</header>

<main>
  {#each items as items}
    <div class="item-list">
      <div class="item-list__img">
        <img alt={items.title} src={items.imgUrl} />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">{items.title}</div>
        <div class="item-list__info-price">{items.price}</div>
        <div class="">{items.description}</div>
        <div class="item-list__info-meta">
          {items.place}
          {calcTime(items.insertAt)}
        </div>
      </div>
    </div>
  {/each}
  <a class="write-btn" href="#/write">+ 글쓰기</a>
</main>
<Footer location="home" />
<div class="media-info-msg">화면 사이즈를 줄여주세요.</div>
