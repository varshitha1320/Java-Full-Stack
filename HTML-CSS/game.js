const gameArea = document.getElementById("game-area");
const basket = document.getElementById("basket");
const scoreDisplay = document.getElementById("score");

let basketX = 160;
const basketSpeed = 20;
let score = 0;

// Move basket with arrow keys
document.addEventListener("keydown", function (e) {
  if (e.code === "ArrowLeft") basketX -= basketSpeed;
  if (e.code === "ArrowRight") basketX += basketSpeed;

  // Keep basket inside game area
  basketX = Math.max(0, Math.min(basketX, 320));
  basket.style.left = basketX + "px";
});

// Create falling candy
function createCandy() {
  const candy = document.createElement("div");
  candy.classList.add("candy");
  candy.style.left = Math.floor(Math.random() * 360) + "px";
  gameArea.appendChild(candy);

  let candyY = 0;
  const fallSpeed = 3;

  function fall() {
    candyY += fallSpeed;
    candy.style.top = candyY + "px";

    // Collision detection
    const basketRect = basket.getBoundingClientRect();
    const candyRect = candy.getBoundingClientRect();

    if (
      basketRect.left < candyRect.right &&
      basketRect.right > candyRect.left &&
      basketRect.top < candyRect.bottom &&
      basketRect.bottom > candyRect.top
    ) {
      score++;
      scoreDisplay.textContent = "Score: " + score;
      candy.remove();
      return;
    }

    // Remove candy if it falls out
    if (candyY > 500) {
      candy.remove();
      return;
    }

    requestAnimationFrame(fall);
  }

  fall();
}

// Drop candies every 1.5 seconds
setInterval(createCandy, 1500);
