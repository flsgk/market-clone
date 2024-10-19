<script>
  export let location; // 첫 번째 선언만 남김
  const moveToHome = () => {
    window.location.hash = "/";
  };
  const moveToMyPage = () => {
    window.location.hash = "/mypage";
  };
</script>

<footer>
  <div class="footer-block">
    <button class="footer-icons" on:click={moveToHome}>
      <div class="footer-icons__img">
        {#if location == "home"}
          <img src="assets/home.svg" alt="home" />
        {:else}
          <img src="assets/home2.svg" alt="home2" />
        {/if}
      </div>
      <div class="footer-icons__desc">홈</div>
    </button>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/newspaper.svg" alt="newspaper" />
      </div>
      <div class="footer-icons__desc">동네생활</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/location.svg" alt="location" />
      </div>
      <div class="footer-icons__desc">내 근처</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/chat.svg" alt="chat" />
      </div>
      <div class="footer-icons__desc">채팅</div>
    </div>
    <button class="footer-icons" on:click={moveToMyPage}>
      <div class="footer-icons__img">
        {#if location == "mypage"}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            class="size-6"
          >
            <path
              fill-rule="evenodd"
              d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
              clip-rule="evenodd"
            />
          </svg>
        {:else}
          <img src="assets/user.svg" alt="" />
        {/if}
      </div>
      <div class="footer-icons__desc">나의 당근</div>
    </button>
  </div>
</footer>
