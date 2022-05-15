/* eslint-disable promise/catch-or-return */
/* eslint-disable jsx-a11y/click-events-have-key-events */
/* eslint-disable jsx-a11y/no-static-element-interactions */
import { useState } from 'react';
import { Col, Container, Row } from 'react-bootstrap';
import DumbbellIcon from 'renderer/assets/Dumbbell';

const videoFeed = 'http://localhost:3001/video_feed';

export default function VideoScreen() {
  const [ex, setEx] = useState(0);

  const changeEx = (theEx: number) => {
    setEx(theEx);

    // // API Call
    // const requestOptions = {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ ex: theEx }),
    // };
    // fetch('http://localhost:3001/', requestOptions).then((response) =>
    //   response.json()
    // );
  };

  return (
    <Container>
      <Col>
        <DumbbellIcon />
        <span className="title">YourFitnessPal</span>
        <span className="sub-title">HawkHacks 2022</span>
        <Row>
          <img className="video-feed" src={videoFeed} alt="Realtime Video" />
        </Row>
        <Row>
          <Col>
            <div
              onClick={() => changeEx(0)}
              className={`button-box ${ex === 0 ? 'selected-button-box' : ''}`}
            >
              <span className="button-title">Push Up</span>
            </div>
          </Col>
          <Col>
            <div
              onClick={() => changeEx(1)}
              className={`button-box ${ex === 1 ? 'selected-button-box' : ''}`}
            >
              <span className="button-title">Bicep Curl</span>
            </div>
          </Col>
          <Col>
            <div
              onClick={() => changeEx(2)}
              className={`button-box ${ex === 2 ? 'selected-button-box' : ''}`}
            >
              <span className="button-title">Squat</span>
            </div>
          </Col>
        </Row>
      </Col>
    </Container>
  );
}
