import React, { useState } from 'react';
import PageTitle from '../components/Typography/PageTitle';
import QrScanner from 'qr-scanner';
import { Modal, ModalHeader, ModalBody, ModalFooter, Button } from '@windmill/react-ui';


function ExpenseAdd() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [qrData, setQrData ] = useState(null);
  const videoReference = React.useRef(null);
  let qrScanner = null;
  
  function openModal() {
    setIsModalOpen(true)
  }
  
  function closeModal() {
    setIsModalOpen(false)
  }

  function setResult(result) {
    setQrData(result.data);
    openModal()
  }

  const startReader = () => {
    console.log(videoReference.current);
    qrScanner = new QrScanner(
      videoReference.current,
      result => setResult(result), {
        highlightScanRegion: true,
        highlightCodeOutline: true,
      }
    );
    qrScanner.start();
  };

  const stopReader = () => {
    if(qrScanner) {
      qrScanner.stop()
    }
  }

  const toggleFlash = () => {
    if(qrScanner) {
      qrScanner.toggleFlash();
    }
  }

  setTimeout(() => {
    startReader()
  }, 200);
  

  return (
    <>
      <PageTitle>Add expense</PageTitle>
      <video ref={videoReference} id='videofromreader'></video>
      <Button size="small" onClick={toggleFlash}>Toggle Flash</Button>

      <Modal isOpen={isModalOpen} onClose={closeModal}>
        <ModalHeader>QRCode read</ModalHeader>
        <ModalBody>
          QRCode read data
          <p>{qrData}</p>
        </ModalBody>
        <ModalFooter>
          <Button className="w-full sm:w-auto" layout="outline" onClick={closeModal}>
            Cancel
          </Button>
          <Button className="w-full sm:w-auto">Accept</Button>
        </ModalFooter>
      </Modal>
    </>
  )
}

export default ExpenseAdd
