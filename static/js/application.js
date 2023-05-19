document.addEventListener('DOMContentLoaded', () => {
  const modal = document.createElement('div'); // 확대되는 이미지를 감싸는 상자
  modal.classList.add('modal');
  document.body.appendChild(modal);

  const images = document.querySelectorAll('.message-img'); // 모든 이미지 요소 선택
  console.log(images);

  images.forEach((img) => {
    console.log(img);
    img.addEventListener('click', () => {
      const modalImg = document.createElement('img'); // 확대되는 이미지
      modalImg.src = img.src;
      modal.appendChild(modalImg);
      modal.style.display = 'flex'; // 상자 보이기
      modalImg.addEventListener('click', () => {
        modal.removeChild(modalImg);
        modal.style.display = 'none'; // 상자 숨기기
      });
    });
  });
});
