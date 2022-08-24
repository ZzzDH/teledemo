package com.group5.opinionmanage.dao;

import com.group5.opinionmanage.entity.Opinions;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * @author 10569
 * @version 1.0
 * @description
 * @Date 2022/8/24 15:07
 */

public interface OpinionsRepository extends JpaRepository<Opinions, Integer> {
    Opinions findByOid(Integer oid);
    List<Opinions> findByContextLike(String context);

    Page<Opinions> findAll(Pageable pageable);
    long count();
}


